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

// SignIn, SignUp 
const SignBaseLayout = Loader(lazy(() => import('layouts/SignBaseLayout')))
const SignUpLayout = Loader(lazy(() => import('layouts/SignUpLayout')))

// DashBoard (Main page)
const DashBoard = Loader(lazy(() => import('content/DashBoard')))

const routes: RouteObject[] = [
  {
    path: '',
    element: <BaseLayout />,
    children: [
      {
        path: '/',
        element: <Navigate to='login' replace />
      },
      {
        path: '/dashboard',
        element: <DashBoard />,
      }
    ]
  },
  {
    path: '/login',
    element: <SignBaseLayout />,
    children: [

    ]
  },
  {
    path: '/signup',
    element: <SignUpLayout />,
  }

]


export default routes