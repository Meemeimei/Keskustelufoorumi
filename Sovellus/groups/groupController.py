from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.groups.forms import GroupForm, AddUserToGroupForm
from Sovellus.posts.forms import PostForm
from Sovellus.posts.models import Post
from Sovellus.groups.models import Group
from Sovellus.users.models import User
from Sovellus.groups.models import Group
from Sovellus.groupUsers.models import Groupuser
from Sovellus.home import homeController

def createGroup():
    form = GroupForm(request.form)
    if not form.validate():
        return homeController.home()
    name = form.name.data
    group = Group.query.filter_by(name=name).first()
    if group:
        return homeController.homeWithCustomError("Group name must be unique")

    group = Group(name)
    db.session().add(group)
    db.session().commit()
    groupUser = Groupuser(current_user.id, group.id)
    db.session().add(groupUser)
    db.session().commit()

    return homeController.homeWithCustomMessage("Group created successfully")

def openGroup(groupId):
    group = Group.query.filter_by(id=groupId).first()
    if not group:
        return homeController.homeWithCustomError("Group doesn't exist or you don't have access to it")
    groupuser = Groupuser.query.filter_by(user_id=current_user.id, group_id=group.id).first()
    if not groupuser and not current_user.admin:
        return homeController.homeWithCustomError("Group doesn't exist or you don't have access to it")

    return render_template("group/index.html", group = group, posts=Post.query.filter(Post.group_id == group.id), postForm = PostForm(), AddUserToGroupForm = AddUserToGroupForm(), users = Group.getUsers(groupId))

def deleteGroup(groupId):

    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")

    Group.query.filter_by(id=groupId).delete()
    Groupuser.query.filter_by(group_id=groupId).delete()
    Post.deleteGroupPosts(groupId)
    db.session().commit()

    return homeController.homeWithCustomMessage("Group removed successfully")

def canSeeGroupPost(groupId, userId):
    group = Group.query.filter_by(id=groupId).first()
    groupuser = Groupuser.query.filter_by(user_id=current_user.id, group_id=group.id).first()
    if not groupuser:
        return False

    return True

def addUserToGroup(groupId):
    if not canSeeGroupPost(groupId, current_user.id):
        return homeController.homeWithCustomError("You need to be a member in the group to complete this operation")

    form = AddUserToGroupForm(request.form)
    if not form.validate():
        return homeController.home()


    username = form.username.data

    user = User.query.filter_by(username=username).first()
    if not user:
        return homeController.homeWithCustomError("user not found")
    groupUser = Groupuser(user.id, groupId)
    db.session().add(groupUser)
    db.session().commit()

    return openGroup(groupId)

def removeUserFromGroup(groupId, userId):
    if not canSeeGroupPost(groupId, current_user.id) and not current_user.admin:
        return homeController.homeWithCustomError("You need to be a member in the group to complete this operation")

    Groupuser.query.filter_by(user_id=userId, group_id=groupId).delete()
    db.session.commit()

    #Empty groups will be automatically deleted
    if Group.isEmpty(groupId):
        deleteGroup(groupId)

    return openGroup(groupId)
