const Home = {
    template: `
    <div>
        <h1>Home</h1>
    </div>
    `
}



const routes = [
    {path : '/', component : Home},
    {path : '/login', component : Login},
    {path : '/register', component : Register},
]


const router = new VueRouter({
    routes
})

export default router;