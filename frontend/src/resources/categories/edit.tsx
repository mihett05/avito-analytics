import React from 'react'
import { Edit, SimpleForm, TextInput } from 'react-admin'

const CategoriesEdit = () => {
  return (
    <Edit>
      <SimpleForm>
        <TextInput source="id" label="id" />
        <TextInput source="key" disabled />
        <TextInput source="name" />
        <TextInput source="parent_id" />
      </SimpleForm>
    </Edit>
  )
}

export default CategoriesEdit