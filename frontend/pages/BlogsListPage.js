export default {
    template: `
      <div>
        <h1>Blogs List</h1>
        <h3 v-for="blog in blogs" >{{ blog.title }}</h3>
      </div>
    `,
    data() {
      return {
        blogs: []
      }
    },
    async mounted() {
      try {
        const res = await fetch(location.origin + '/api/blogs', {
          headers: {
            'Authentication-Token': JSON.parse(localStorage.getItem('user')).token
          }
        });
        
        if (res.ok) {
          this.blogs = await res.json();  // Store the blog data in blogs array
        } else {
          console.error('Failed to fetch blogs:', res.status);
        }
      } catch (error) {
        console.error('Error fetching blogs:', error);
      }
    }
  }
  