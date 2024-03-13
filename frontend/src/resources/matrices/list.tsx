import React from 'react';
import { List, Datagrid, TextField } from 'react-admin';

export const MatricesList = () => (
  <List>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="type" />
      <TextField source="segment_id" />
    </Datagrid>
  </List>
);

export default MatricesList;
