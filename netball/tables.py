# import django_tables2 as tables
# from django_tables2.utils import A
# from netball.models import *
#
# from netball.models import *
from table import Table
from table.columns import Column
from netball.models import *

# class  PoolTable(tables.Table):
#     pool_id = tables.LinkColumn('pool_id', args=[A('pk')])
#     pool_name = tables.LinkColumn('pool_name', args=[A('pk')])
#
#     class Meta:
#         model = Pool
#         fields = ('pool_id', 'pool_name')
#         attrs = {"class": "table-striped table-bordered"}
#         empty_text = "There are no customers matching the search criteria..."

# class  PoolTable(Table):
#     pool_id = Column(field='pool_id',header='ID')
#     pool_name = Column(field='pool_name',header='Pool_Name')
#     #status = Column(field='status',header='Status')
#     view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'view'},sortable=False)
#     edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit','title':'edit'},sortable=False)
#     trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
#                                                    'data-target':"{% url 'netball:delete_pool' %}",'title':'delete'},sortable=False)
#
#
#     class Meta:
#         model = Pool
