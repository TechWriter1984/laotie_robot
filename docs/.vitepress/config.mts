import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: /repo/,
  title: "Laotie",
  description: "Laotie robot",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: '/laotie.gif',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' },
      { text: 'Chassis', link: '/chassis' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' },
          { text: 'Chassis', link: '/chassis'}
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/TechWriter1984/laotie_robot/tree/develop' }
    ]
  }
})
