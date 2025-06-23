import type { AddUserResponse } from "./addUser";

export const DeleteUserService = async (userId: string): Promise<boolean> => {
  try {
    await $fetch(`http://127.0.0.1:8000/api/user/delete/${userId}`, {
      method: "DELETE",
    });
    return true;
  } catch {
    return false;
  }
}; 