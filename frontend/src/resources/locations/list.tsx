import React from 'react';
import { Title, useGetList } from 'react-admin';
import type { Location } from './entity';

function LocationsList() {
  const { data, total, isLoading } = useGetList<Location>('locations', {});
  return (
    <div>
      <Title title="Список локации"></Title>
    </div>
  );
}

export default LocationsList;
