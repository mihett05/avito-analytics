import React from 'react';
import { Create, SimpleForm, TextInput, FileInput, FileField } from 'react-admin';

function MatrixCreate() {
  return (
    <Create>
      <SimpleForm>
        <TextInput source="name" required />
        <TextInput source="segment_id" required />
        <FileInput source="file" isRequired />
      </SimpleForm>
    </Create>
  );
}

export default MatrixCreate;
