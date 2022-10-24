import { ReactNode } from "react";
import { createSlice } from "@reduxjs/toolkit";

import { RootState } from "app/store";
import { fetchGetUserInfo } from "./fetchUserInfo";
import { UserInfo } from "./userInfoTypes";

interface UserInfoState {
    informations: UserInfo[];
    status: "idle" | "loading" | "succeeeded" | "failed";
    error: string | null;
    increment: number;
}

const initialState: UserInfoState = {
    informations: [],
    status: "idle",
    error: null,
    increment: 0,
}

export const userInfoSlice = createSlice({
    name: 'userInfo',
    initialState,
    reducers: {
        increment(state: UserInfoState) {
            state.increment += 1;
        },
    },
    extraReducers: (builder) => {
        builder.addCase(fetchGetUserInfo.pending, (state) => {
            state.status = 'loading';
            state.error = null;
        });
        builder.addCase(fetchGetUserInfo.fulfilled, (state, {payload}) => {
            state.informations.push(...[payload]);
            state.status = 'idle';
        });
        builder.addCase(fetchGetUserInfo.rejected, (state, {payload}) => {
            console.log("rejected", payload)
            if (payload) state.error = payload.message;
            state.status = 'failed';
        });
    },
});

export const { increment } = userInfoSlice.actions;

export const selectUserInfo = (state: RootState) => {
    return state.userInfo.informations;
};

export default userInfoSlice.reducer ;
// export default userInfoSlice;