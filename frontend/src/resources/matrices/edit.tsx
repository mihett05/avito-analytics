import React from 'react';
import {
  Datagrid,
  Edit,
  List,
  NumberField,
  NumberInput,
  ReferenceManyField,
  SimpleForm,
  TextInput,
} from 'react-admin';

const MatrixEdit = () => {
  return (
    <Edit>
      <SimpleForm>
        <NumberInput source="id" />
        <TextInput source="name" />
        <TextInput source="type" />
        <NumberInput source="segment_id" />
        <List>
          <ReferenceManyField reference="price" target="matrix_id">
            <Datagrid>
              <NumberField source="matrix_id" />
              <NumberField source="category_id" />
              <NumberField source="location_id" />
              <NumberField source="price" />
            </Datagrid>
          </ReferenceManyField>
        </List>
      </SimpleForm>
    </Edit>
  );
};

export default MatrixEdit;
