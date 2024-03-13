import React from 'react';
import {
  Datagrid,
  Edit,
  List,
  NumberField,
  NumberInput,
  Pagination,
  ReferenceManyField,
  SelectInput,
  SimpleForm,
  TextInput,
} from 'react-admin';

const MatrixEdit = () => {
  return (
    <Edit>
      <SimpleForm>
        <NumberInput source="id" disabled />
        <TextInput source="name" />
        <SelectInput
          source="type"
          choices={[
            { id: 'BASE', name: 'Основная' },
            { id: 'DISCOUNT', name: 'Скидочная' },
          ]}
          isRequired
        />

        <NumberInput source="segment_id" />

        <ReferenceManyField reference="price" target="matrix_id" pagination={<Pagination />}>
          <Datagrid>
            <NumberField source="matrix_id" />
            <NumberField source="category_id" />
            <NumberField source="location_id" />
            <NumberField source="price" />
          </Datagrid>
        </ReferenceManyField>
      </SimpleForm>
    </Edit>
  );
};

export default MatrixEdit;
