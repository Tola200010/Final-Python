"""Initial migration.

Revision ID: 857578683703
Revises: 
Create Date: 2021-08-18 06:47:05.266820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '857578683703'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('code', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('username')
    )
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('contact', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('contact', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('limit_student', sa.INTEGER(), nullable=True),
    sa.Column('teacher_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrollment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('student_id', sa.INTEGER(), nullable=True),
    sa.Column('course_id', sa.INTEGER(), nullable=True),
    sa.Column('payment', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enrollment')
    op.drop_table('course')
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('users')
    # ### end Alembic commands ###