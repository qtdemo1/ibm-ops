"""Initial revision

Revision ID: 9c64c3521fc1
Revises: 
Create Date: 2021-10-15 11:38:32.332937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c64c3521fc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deployed_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('modified_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_id'), 'model', ['id'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.NCHAR(length=32), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('endpoint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.NCHAR(length=128), nullable=False),
    sa.Column('deployed_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_endpoint_id'), 'endpoint', ['id'], unique=True)
    op.create_table('model_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('configuration', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_config_id'), 'model_config', ['id'], unique=True)
    op.create_table('binary_ml_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_b64', sa.LargeBinary(), nullable=False),
    sa.Column('input_data_structure', sa.Enum('AUTO', 'DATAFRAME', 'NUMPY_ARRAY', 'DMATRIX', 'LIST', name='modelinput'), nullable=False),
    sa.Column('output_data_structure', sa.Enum('AUTO', 'NUMPY_ARRAY', 'DATAFRAME', 'LIST', name='modeloutput'), nullable=False),
    sa.Column('format', sa.Enum('PICKLE', 'JOBLIB', 'PMML', 'BST', name='modelwrapper'), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['endpoint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_binary_ml_model_id'), 'binary_ml_model', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_binary_ml_model_id'), table_name='binary_ml_model')
    op.drop_table('binary_ml_model')
    op.drop_index(op.f('ix_model_config_id'), table_name='model_config')
    op.drop_table('model_config')
    op.drop_index(op.f('ix_endpoint_id'), table_name='endpoint')
    op.drop_table('endpoint')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_model_id'), table_name='model')
    op.drop_table('model')
    # ### end Alembic commands ###
