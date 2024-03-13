import React from 'react';
import { List, Datagrid, TextField } from 'react-admin';
import Storage from './storage';

export const MatricesList = () => (
  <List empty={false} aside={<Storage />}>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="type" />
      <TextField source="segment_id" />
    </Datagrid>
  </List>
);

export default MatricesList;
