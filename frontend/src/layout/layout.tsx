import React from 'react';
import { Layout, LayoutProps } from 'react-admin';
import CustomMenu from './menu';

const CustomLayout = (props: LayoutProps) => <Layout {...props} menu={CustomMenu} />;

export default CustomLayout;
