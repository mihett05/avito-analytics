import { Autocomplete, Box, CircularProgress, TextField } from '@mui/material';
import React from 'react';
import { SimpleForm, useDataProvider, useGetMany, useGetOne, useList } from 'react-admin';
import { useQuery } from 'react-query';
import type { Node } from '~/entities';
import { Matrix } from '~/entities/matrix';

function StoragePage() {
  useQuery('matrix', () => getMatrix);
  const { data, isLoading, error } = useGetMany<Matrix>('matrix');
  // const {
  //   data: locations,
  //   isLoading: isLocationsLoading,
  //   error: locationsError,
  // } = useGetMany<Node>('location');
  // const {
  //   data: categories,
  //   isLoading: isCategoriesLoading,
  //   error: categoriesError,
  // } = useGetMany<Node>('category');

  if (isLoading) {
    return <CircularProgress />;
  }

  if (error) {
    return <h1>Не удалось загрузить список матриц</h1>;
  }

  console.log(data, isLoading, error);

  return (
    <Box>
      <Autocomplete
        options={
          data?.map((matrix) => ({
            id: matrix.id,
            label: matrix.name,
          })) || []
        }
        renderInput={(params) => <TextField {...params} label="Матрица" />}
      />
    </Box>
  );
}

export default StoragePage;
