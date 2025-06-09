// stores/userid.ts

export const useUserIdStore = defineStore('userid', {
  state: () => ({
    userId: null as string | null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.userId,
  },
  actions: {
    setUserId(userId:string) {
      this.userId = userId;
    },
    clearUserId() {
      this.userId = null;
    },
    getUserId(){
      return this.userId;
    }
  },
});