import { ReactNode } from "react";

export interface UserInfo {
    children?: ReactNode
    data: {
        id: number,
        name: string,
        email: string,
        password: string,
        public_id: string,
        own_donation_mount: number,
        qt_id: number[],
        comments_id: number[],
        challenges_id: number[],
        donation_id: number[],
        created_at: string,
        updated_at: string,
    };
    type: string;
}