import { Link } from 'react-router-dom';

import { Box, Container, Grid, Typography } from "@mui/material";

import { useAppDistpatch, useAppSelector } from 'app/hooks';
import { useEffect } from 'react';
import { fetchGetUserInfo } from 'features/users/fetchUserInfo';
import { selectUserInfo } from 'features/users/userInfoSlice';
import { UserInfo } from 'features/users/userInfoTypes';


function DashBoard() {
  const dispatch = useAppDistpatch();

  useEffect(() => {
    dispatch(fetchGetUserInfo({}));
  }, []);

  const usersInfo = useAppSelector(selectUserInfo)
  const userStatus = useAppSelector((state) => state.userInfo.status);

  console.log(usersInfo)
  return (
    <Box>
      {userStatus === 'loading' ? (
        "Loading..."
      ) : (
        "test"
      )}
    </Box>
  );
}

export default DashBoard