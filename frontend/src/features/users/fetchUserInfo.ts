import { createAsyncThunk } from "@reduxjs/toolkit";

import {client} from 'api/client';
import { UserInfo } from "./userInfoTypes";

type FetchUserInfoError = {
  message: string,
}

export const fetchGetUserInfo = createAsyncThunk<
  UserInfo,
  {},
  { rejectValue: FetchUserInfoError }
> ("fetchUserInfo/fetchGetUserInfo",
  async (payload, thunkApi) => {
    const response = await client.get(`/user/`);
    if (response.status !== 200) {
      console.log("rejected!!");
      return thunkApi.rejectWithValue({
        message: "Failed to fetch UserInfo",
      });
    };

    // const data = await response.json();
    // return data.value;

    return response.data;
  });