import React from 'react';
import { List, Datagrid, TextField } from 'react-admin';

export const MatriciesList = () => (
  <List>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="type" />
      <TextField source="segment_id" />
    </Datagrid>
  </List>
);

export default MatriciesList;
