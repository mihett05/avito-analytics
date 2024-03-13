import React from 'react';
import { Menu } from 'react-admin';

function CustomMenu() {
  return (
    <Menu>
      <Menu.DashboardItem />
      <Menu.ResourceItem name="location" />
      <Menu.ResourceItem name="category" />
      <Menu.ResourceItem name="price" />
      <Menu.ResourceItem name="matrix" />
    </Menu>
  );
}

export default CustomMenu;