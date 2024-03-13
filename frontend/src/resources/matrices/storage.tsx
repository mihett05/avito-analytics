import React, { useEffect, useMemo, useState } from 'react';
import { useQuery } from 'react-query';
import { Autocomplete, Box, CircularProgress, Switch, TextField, Typography } from '@mui/material';
import { SimpleForm, useDataProvider, useGetMany, useGetOne, useList } from 'react-admin';
import type { Node } from '~/entities';
import { Matrix } from '~/entities/matrix';
import { getStorage } from '~/api/storage';

type MatrixValue = { id: number; label: string };
interface FieldProps {
  value: number | null;
  onChange: (value: number) => any;
}

const BaselineAutoComplete = ({ value, onChange }: FieldProps) => {
  const dataProvider = useDataProvider();
  const { data, isLoading, error } = useQuery(
    ['matrix', 'useGetMany'],
    () => dataProvider.getMany('matrix', {}) as Promise<{ data: Matrix[] }>,
  );
  const matrices = useMemo(
    () => (data ? data.data.filter((matrix) => matrix.type === 'BASE') : []),
    [data],
  );
  const index = useMemo(() => matrices.findIndex((el) => el.id === value), [data, value]);

  if (isLoading) {
    return <CircularProgress />;
  }

  if (error || !data) {
    return <h1>Не удалось загрузить список матриц</h1>;
  }

  const options = (matrices.map((matrix) => ({
    id: matrix.id,
    label: matrix.name,
  })) || []) as MatrixValue[];

  return (
    <Autocomplete
      value={index === -1 ? null : { id: matrices[index].id, label: matrices[index].name }}
      options={options}
      onChange={(_, newValue: MatrixValue | null) => {
        newValue !== null && onChange(newValue.id);
      }}
      renderInput={(params) => <TextField {...params} label="Baseline матрица" />}
      isOptionEqualToValue={(option, v) => option.id === v.id}
    />
  );
};

interface DiscountsSwitchesProps {
  value: number[];
  onChange: (value: number[]) => any;
}

const DiscountsSwitches = ({ value, onChange }: DiscountsSwitchesProps) => {
  const dataProvider = useDataProvider();
  const { data, isLoading, error } = useQuery(
    ['matrix', 'useGetMany'],
    () => dataProvider.getMany('matrix', {}) as Promise<{ data: Matrix[] }>,
  );
  const matirces = useMemo(
    () => (data ? data.data.filter((matrix) => matrix.type === 'DISCOUNT') : []),
    [data],
  );

  if (isLoading) {
    return <CircularProgress />;
  }

  if (error || !data) {
    return <h1>Не удалось загрузить список матриц</h1>;
  }

  return (
    <Box>
      {matirces.map((matrix) => (
        <Box
          key={matrix.id}
          sx={{
            display: 'flex',
          }}
        >
          <Typography>{matrix.name}</Typography>
          <Switch
            checked={value.includes(matrix.id)}
            onChange={() => {
              if (value.includes(matrix.id)) {
                onChange(value.filter((id) => id !== matrix.id));
              } else {
                onChange([...value, matrix.id]);
              }
            }}
          />
        </Box>
      ))}
    </Box>
  );
};

function Storage() {
  const { data, isLoading, error } = useQuery('storage', () => getStorage());

  const [form, setForm] = useState<{ baseline: number | null; discounts: number[] }>({
    baseline: null,
    discounts: [],
  });

  useEffect(() => {
    if (data && data !== null && !isLoading && !error) {
      setForm({
        ...form,
        baseline: data.baseline,
        discounts: data.discounts,
      });
    }
  }, [data, isLoading, error]);

  if (isLoading) {
    return <CircularProgress />;
  }

  if (error) {
    return <h1>Не удалось загрузить список матриц</h1>;
  }

  console.log(form);

  return (
    <Box
      sx={{
        width: 300,
      }}
    >
      <BaselineAutoComplete
        value={form.baseline}
        onChange={(value) =>
          setForm((newForm) => ({
            ...newForm,
            baseline: value,
          }))
        }
      />
      <DiscountsSwitches
        value={form.discounts}
        onChange={(value) =>
          setForm((newForm) => ({
            ...newForm,
            discounts: value,
          }))
        }
      />
    </Box>
  );
}

export default Storage;
