#!/usr/bin/env python
"""
初始化 SQLite 数据库，导入初始数据
"""
import asyncio
from datetime import datetime
from config.database import async_engine
from config.database import Base
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.do.user_do import SysUser, SysUserRole, SysUserPost
from module_admin.entity.do.post_do import SysPost
from module_admin.entity.do.role_do import SysRole, SysRoleMenu
from module_admin.entity.do.menu_do import SysMenu
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async def init_database():
    """初始化数据库"""
    # 创建所有表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 创建 Session
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        # 部门数据
        depts = [
            SysDept(dept_id=100, parent_id=0, ancestors='0', dept_name='集团总公司', order_num=0,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
            SysDept(dept_id=101, parent_id=100, ancestors='0,100', dept_name='深圳分公司', order_num=1,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
            SysDept(dept_id=102, parent_id=100, ancestors='0,100', dept_name='长沙分公司', order_num=2,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
            SysDept(dept_id=103, parent_id=101, ancestors='0,100,101', dept_name='研发部门', order_num=1,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
            SysDept(dept_id=104, parent_id=101, ancestors='0,100,101', dept_name='市场部门', order_num=2,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
            SysDept(dept_id=105, parent_id=101, ancestors='0,100,101', dept_name='测试部门', order_num=3,
                   leader='年糕', phone='15888888888', email='niangao@qq.com', status='0', del_flag='0',
                   create_by='admin', create_time=datetime.now()),
        ]
        session.add_all(depts)

        # 岗位数据
        posts = [
            SysPost(post_id=1, post_code='ceo', post_name='董事长', post_sort=1, status='0',
                   create_by='admin', create_time=datetime.now()),
            SysPost(post_id=2, post_code='se', post_name='项目经理', post_sort=2, status='0',
                   create_by='admin', create_time=datetime.now()),
            SysPost(post_id=3, post_code='hr', post_name='人力资源', post_sort=3, status='0',
                   create_by='admin', create_time=datetime.now()),
            SysPost(post_id=4, post_code='user', post_name='普通员工', post_sort=4, status='0',
                   create_by='admin', create_time=datetime.now()),
        ]
        session.add_all(posts)

        # 用户数据（admin 密码：123456）
        users = [
            SysUser(
                user_id=1, dept_id=103, user_name='admin', nick_name='超级管理员',
                user_type='00', email='niangao@163.com', phonenumber='15888888888',
                sex='1', password='$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2',
                status='0', del_flag='0', create_by='admin', create_time=datetime.now(),
                pwd_update_date=datetime.now(), remark='管理员'
            ),
            SysUser(
                user_id=2, dept_id=105, user_name='niangao', nick_name='年糕',
                user_type='00', email='niangao@qq.com', phonenumber='15666666666',
                sex='1', password='$2a$10$7JB720yubVSZvUI0rEqK/.VqGOZTH.ulu33dHOiBE8ByOhJIrdAu2',
                status='0', del_flag='0', create_by='admin', create_time=datetime.now(),
                pwd_update_date=datetime.now(), remark='测试员'
            ),
        ]
        session.add_all(users)

        # 角色数据
        roles = [
            SysRole(role_id=1, role_name='超级管理员', role_key='admin', role_sort=1, status='0',
                   create_by='admin', create_time=datetime.now(), remark='超级管理员'),
            SysRole(role_id=2, role_name='普通角色', role_key='common', role_sort=2, status='0',
                   create_by='admin', create_time=datetime.now(), remark='普通角色'),
        ]
        session.add_all(roles)

        # 菜单数据
        menus = [
            SysMenu(menu_id=1, menu_name='系统管理', parent_id=0, order_num=1, path='system', component='',
                   route_name='System', is_frame=1, is_cache=0, menu_type='M', visible='0', status='0',
                   icon='system', create_by='admin', create_time=datetime.now()),
            SysMenu(menu_id=100, menu_name='用户管理', parent_id=1, order_num=1, path='user',
                   component='system/user/index', route_name='User', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='user', perms='system:user:list', create_by='admin',
                   create_time=datetime.now()),
            SysMenu(menu_id=101, menu_name='部门管理', parent_id=1, order_num=2, path='dept',
                   component='system/dept/index', route_name='Dept', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='dept', perms='system:dept:list', create_by='admin',
                   create_time=datetime.now()),
            SysMenu(menu_id=102, menu_name='岗位管理', parent_id=1, order_num=3, path='post',
                   component='system/post/index', route_name='Post', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='post', perms='system:post:list', create_by='admin',
                   create_time=datetime.now()),
            SysMenu(menu_id=103, menu_name='角色管理', parent_id=1, order_num=4, path='role',
                   component='system/role/index', route_name='Role', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='role', perms='system:role:list', create_by='admin',
                   create_time=datetime.now()),
            SysMenu(menu_id=104, menu_name='菜单管理', parent_id=1, order_num=5, path='menu',
                   component='system/menu/index', route_name='Menu', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='menu', perms='system:menu:list', create_by='admin',
                   create_time=datetime.now()),
            SysMenu(menu_id=105, menu_name='字典管理', parent_id=1, order_num=6, path='dict',
                   component='system/dict/index', route_name='Dict', is_frame=1, is_cache=0, menu_type='C',
                   visible='0', status='0', icon='dict', perms='system:dict:list', create_by='admin',
                   create_time=datetime.now()),
        ]
        session.add_all(menus)

        # 用户-角色关联
        user_roles = [
            SysUserRole(user_id=1, role_id=1),  # admin用户关联超级管理员角色
            SysUserRole(user_id=2, role_id=2),  # niangao用户关联普通角色
        ]
        session.add_all(user_roles)

        # 用户-岗位关联
        user_posts = [
            SysUserPost(user_id=1, post_id=1),  # admin用户关联董事长岗位
            SysUserPost(user_id=2, post_id=4),  # niangao用户关联普通员工岗位
        ]
        session.add_all(user_posts)

        # 角色-菜单关联（超级管理员拥有所有菜单权限）
        role_menus = [
            SysRoleMenu(role_id=1, menu_id=1),
            SysRoleMenu(role_id=1, menu_id=100),
            SysRoleMenu(role_id=1, menu_id=101),
            SysRoleMenu(role_id=1, menu_id=102),
            SysRoleMenu(role_id=1, menu_id=103),
            SysRoleMenu(role_id=1, menu_id=104),
            SysRoleMenu(role_id=1, menu_id=105),
            # 普通角色只有部分菜单权限
            SysRoleMenu(role_id=2, menu_id=1),
            SysRoleMenu(role_id=2, menu_id=100),
        ]
        session.add_all(role_menus)

        await session.commit()
        print('✅ 数据库初始化成功！')
        print('默认用户：')
        print('  账号：admin  密码：123456')
        print('  账号：niangao  密码：123456')


if __name__ == '__main__':
    asyncio.run(init_database())
