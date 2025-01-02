export default {
    template: `
    <div>
        <h1>Login</h1>
        <input type="text" placeholder="Username" v-model="username">
        <input type="password" placeholder="Password" v-model="password">
        <button @click="login">Login</button>`
}