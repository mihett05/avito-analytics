import React from 'react';
import { List, Datagrid, TextField, TopToolbar, ExportButton } from 'react-admin';

import { uploadLocationCsv } from '~/api/locations';
import UploadButton from '~/shared/upload-button';

const ListActions = () => {
  return (
    <TopToolbar>
      <UploadButton onUpload={uploadLocationCsv} />
      <ExportButton />
    </TopToolbar>
  );
};

export const LocationsList = () => (
  <List actions={<ListActions />} empty={false}>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="parent_id" />
      <TextField source="key" />
    </Datagrid>
  </List>
);

export default LocationsList;
