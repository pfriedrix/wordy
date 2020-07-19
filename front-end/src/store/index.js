import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {},
    collections: [],
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, token,) {
      state.status = 'success'
      state.token = token
    },
    auth_error(state) {
      state.status = 'error'
    },
    logout(state) {
      state.status = ''
      state.token = ''
    },
    user(state) {
      state.user = ''
    }
  },
  actions: {
    getToken({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.post('/auth/login', payload)
          .then(resp => {
            const token = resp.data.access
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
            commit('auth_success', token)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    getUser({ commit }) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.get('/user')
          .then(resp => {
            if (resp.data.is_confirmed === false) {
              localStorage.removeItem('token')
            }
            commit('user')
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            reject(err)
          })
      })
    },
    editUser({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.put('/user', payload)
          .then(resp => {
            commit('user')
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error')
            reject(err)
          })
      })
    },
    createToken({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.post('/auth/sign-up', payload)
          .then(resp => {
            const token = resp.data.token.access
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
            commit('auth_success', token)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    getCollections({ commit }) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.get('/collections/')
          .then(resp => {
            this.state.collections = resp.data
            resolve(resp)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    getCollection({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.get('/collections/' + payload['collection'] + '/')
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    createCollection({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.post('/collections/',
          payload
        )
          .catch(err => reject(err))
      })
    },
    delCollection({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.delete('/collections/' + payload + '/')
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    editCollection({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.put('/collections/' + payload['collection'] + '/', {
          title: payload['title'],
          user: payload['user'],
        })
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    getWords({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.get('/collections/' + payload['collection'] + '/words')
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    getRandomWords({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.get('/collections/' + payload['collection'] + '/get-random-order')
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    createWord({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.post('/collections/' + payload['collection'] + '/words', {
          user: payload['user'],
          collection: payload['collection'],
          title: payload['title'],
          translation: payload['translation'],
        })
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    editWord({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.put('/words/' + payload['word'] + '/', {
          user: payload['user'],
          collection: payload['collection'],
          title: payload['title'],
          translation: payload['translation'],
        })
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    translate({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.post('/translator',{
          title: payload['title'],
        })
          .then(resp => resolve(resp))
          .catch(err => reject(err))
      })
    },
    delete({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.delete('/words/' + payload['word'] + '/')
        .then(resp => resolve(resp))
        .catch(err => reject(err))
      })
    },
    getOptions({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.get('/words/' + payload['word'] + '/options')
        .then(resp => resolve(resp))
        .catch(err => reject(err))
      })
    },
    learnWord({commit}, payload) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
        axios.post('/words/' + payload['word'] + '/learn')
        .then(resp => resolve(resp))
        .catch(err => reject(err))
      })
    },
},
  getters: {
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
}
})
