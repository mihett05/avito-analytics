import React from 'react';
import { List, Datagrid, TextField } from 'react-admin'

export const LocationsList = () => (
  <List>
      <Datagrid rowClick="edit">
          <TextField source="id" />
          <TextField source="key" />
          <TextField source="name" />
          <TextField source="parent_id" />
      </Datagrid>
  </List>
);

export default LocationsList;