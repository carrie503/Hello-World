
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'test'
down_revision = 'test'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("UPDATE user SET is_mobile_visible = '1'")


def downgrade():
    op.alter_column(
        'user',
        'is_mobile',
        type_=sa.Boolean(create_constraint=False),
        nullable=False,
        server_default='0',
    )
