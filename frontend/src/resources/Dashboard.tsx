import { Card, CardContent, CircularProgress, Typography } from '@mui/material'
import { BarChart, LineChart, PieChart } from '@mui/x-charts'
import React from 'react'
import { Title } from 'react-admin'
import { useQuery } from 'react-query'
import { api } from '~/api/api'

const getAnalyticsInfo = async () => {
  return await api.get('storage/analytics')
}

const Dashboard = () => {  
  const { data, isLoading, isError } = useQuery("dataStorage", () => getAnalyticsInfo());
  const obj = data?.data;
  if (isLoading || isError) {
    return <CircularProgress />
  }
  console.log(obj?.total_requests);
  const d = Object.keys(obj?.categories).map((key) => { return (key) })
  console.log(d);
  const dataset = Object.keys(obj.categories).map((key) => { return ({[key]: obj.categories[key]}) })
  console.log(dataset);

  return (
    <Card>
      <Title title="Главная страница"/>
      <CardContent>
        {
          isLoading ?
          <CircularProgress />
          : isError ?
          <Typography>Error!</Typography>
          :
          <div>
            <BarChart
              xAxis={[{ scaleType: 'band', data: ['group A', 'group B', 'group C'] }]}
              series={[{ data: [4, 3, 5] }, { data: [1, 6, 3] }, { data: [2, 5, 6] }]}
              width={500}
              height={300}
            />
            <LineChart
              xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
              series={[
                {
                  data: [2, 5.5, 2, 8.5, 1.5, 5],
                },
              ]}
              width={500}
              height={300}
            />
            <PieChart
              series={[
                {
                  data: [
                    { id: 0, value: 10, label: 'series A' },
                    { id: 1, value: 15, label: 'series B' },
                    { id: 2, value: 20, label: 'series C' },
                  ],
                },
              ]}
              width={400}
              height={200}
            />
          </div>
        }
      </CardContent>
    </Card>
  )
}

export default Dashboard