import { Box, Grid } from "@mui/material";

import { useAppDistpatch, useAppSelector } from 'store/hooks/hooks';
import { useEffect } from 'react';
import { fetchGetUserInfo } from 'store/features/users/fetchUserInfo';
import { selectUserInfo } from 'store/features/users/userInfoSlice';
import { UserInfo } from 'store/features/users/userInfoTypes';

import UserInfoData from 'components/userInfo';
import CurrentStatusBoard from 'components/Dashboard/CurrentStatusBoard';
import MyQTBoard from "components/Dashboard/MyQTBoard";

function DashBoard() {
  const dispatch = useAppDistpatch();
  const usersInfo = useAppSelector(selectUserInfo)
  const userStatus = useAppSelector((state) => state.userInfo.status);

  useEffect(() => {
    dispatch(fetchGetUserInfo({}));
  }, []);
  console.log(usersInfo)
  return (
    <Box sx={{ width: '100%' }}>
      {/* {userStatus === 'loading' ? (
        "Loading..."
      ) : (
        <>
          {usersInfo.map((value: any, index: any) => `${value.data[`${index}`]['email']}`)}
        </>
        // <UserInfoData userInfo={usersInfo} />
      )} */}

      <Grid
        container
        direction="row"
        rowSpacing={2}
        columnSpacing={{
          mobile: 1,
          tablet: 2,
          desktop: 3
        }}
        justifyContent="center"
        alignItems="stretch"
        sx={{ minHeight: "300px" }}
      >
        <Grid item mobile={4} >
          <CurrentStatusBoard />
        </Grid>
        <Grid item mobile={8}>
          <MyQTBoard />
        </Grid>
        <Grid item mobile={4}>
          진행 중인 챌린지
        </Grid>
        <Grid item mobile={8}>
          댓글
        </Grid>

      </Grid>
    </Box>
  );
}

export default DashBoard