// stores/userid.ts

export const useUserIdStore = defineStore('userid', {
  state: () => ({
    userId: null as number | null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.userId,
  },
  actions: {
    setUserId(userId:number) {
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