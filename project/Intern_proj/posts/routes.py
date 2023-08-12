from flask import Blueprint
from flask import render_template, url_for, flash, redirect,request,abort,Blueprint
from flask_login import  current_user,login_required
from Intern_proj import db
from Intern_proj.models import Post
from Intern_proj.posts.forms import PostForm
from Intern_proj.posts.utils import save_picture_p,get_embed_link




posts=Blueprint('posts',__name__)

@posts.route("/new.post", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit(): 
        if form.image_file.data:
            picture_file = save_picture_p(form.image_file.data)
        if form.video_link.data:
            embed_link=get_embed_link(form.video_link.data) 
        else:
            embed_link=None
        post=Post( title=form.title.data  ,image_file=picture_file, content=form.content.data,user_id=current_user.id,video_link=embed_link)
        db.session.add(post)
        db.session.commit()
        flash(f'Your Post has been added', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Account',form=form)


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/author/<int:post_id>")
def author(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('author.html', title=post.title, post=post)
