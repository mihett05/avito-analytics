import React from 'react';
import { Menu } from 'react-admin';

function CustomMenu() {
  return (
    <Menu>
      <Menu.DashboardItem />
      <Menu.ResourceItem name="matrix" />
      <Menu.ResourceItem name="location" />
      <Menu.ResourceItem name="category" />
    </Menu>
  );
}

export default CustomMenu;
