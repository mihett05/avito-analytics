import React from 'react';
import { List, Datagrid, TextField, TopToolbar, ExportButton } from 'react-admin';
import { uploadCategotyCsv } from '~/api/categories';
import UploadButton from '~/shared/upload-button';

const ListActions = () => {
  return (
    <TopToolbar>
      <UploadButton onUpload={uploadCategotyCsv} />
      <ExportButton />
    </TopToolbar>
  );
};

export const CategoriesList = () => (
  <List actions={<ListActions />} empty={false}>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <TextField source="key" />
      <TextField source="name" />
      <TextField source="parent_id" />
    </Datagrid>
  </List>
);

export default CategoriesList;
