import React from 'react';
import { List, Datagrid, TextField, TopToolbar, ExportButton } from 'react-admin';

export const MatricesList = () => (
  <List empty={false}>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="type" />
      <TextField source="segment_id" />
    </Datagrid>
  </List>
);

export default MatricesList;
