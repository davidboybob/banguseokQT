import { Suspense, lazy } from 'react';
import { RouteObject } from 'react-router';
import { Navigate } from 'react-router-dom';

import SuspenseLoader from 'components/SuspenseLoader';
import BaseLayout from 'layouts/BaseLayouts';

const Loader = (Component: any) => (props: any) => (
  <Suspense fallback={<SuspenseLoader />}>
    <Component {...props} />
  </Suspense>
)

// DashBoard (Main page)
const DashBoard = Loader(lazy(() => import('content/DashBoard')))

const routes: RouteObject[] = [
  {
    path: '',
    element: <BaseLayout />,
    children: [
      {
        path: '/',
        element: <DashBoard />
      }
    ]
  }
]


export default routes