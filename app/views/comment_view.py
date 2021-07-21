from flask import Blueprint, request
from http import HTTPStatus
from app.services.comment_service import create, get, patch, delete
from flask_jwt_extended import get_jwt_identity, jwt_required


bp = Blueprint('bp_comment', __name__, url_prefix="/user")


@bp.post("/artist/<user_id>/image/<image_id>/comment")
@jwt_required()
def create_comment(user_id, image_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    print(current_user)
    print(type(current_user))
    comment = create(data["comment"], current_user["id"], image_id)

    return comment, HTTPStatus.CREATED


@bp.get("/artist/<user_id>/image/<image_id>/comment")
def get_comments(user_id, image_id):
    comments = get(image_id)
    

    return comments, HTTPStatus.OK


@bp.patch("/artist/<user_id>/image/<image_id>/comment/<comment_id>")
@jwt_required()
def patch_comments(user_id, image_id, comment_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    new_comment = patch(data["comment"], comment_id, current_user["id"])

    return new_comment, HTTPStatus.OK


@bp.delete("/artist/<user_id>/image/<image_id>/comment/<comment_id>")
@jwt_required()
def delete_comments(user_id, image_id, comment_id):
    current_user = get_jwt_identity()

    new_comment = delete(comment_id, current_user["id"])

    return new_comment, HTTPStatus.NO_CONTENT