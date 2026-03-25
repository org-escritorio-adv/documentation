import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Advocacia - Documentação',
  tagline: 'Documentação do projeto',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://org-escritorio-adv.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/documentation/',

  organizationName: 'org-escritorio-adv', // Usually your GitHub org/user name.
  projectName: 'documentation', // Usually your repo name.

  trailingSlash: false,
  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'throw', // ou 'throw' / 'ignore'
    },
  },

  deploymentBranch: "gh-pages",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themes: [
    [
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      require.resolve("@easyops-cn/docusaurus-search-local"),
      ({
        // ... Your options.
        // `hashed` is recommended as long-term-cache of index file is possible.
        hashed: true,
        // For Docs using Chinese, it is recomended to set:
        // language: ["en", "zh"],
        language: ["pt"], // busca em português
        // Customize the keyboard shortcut to focus search bar (default is "mod+k"):
        // searchBarShortcutKeymap: "s", // Use 'S' key
        searchBarShortcutKeymap: "ctrl+shift+f", // Use Ctrl+Shift+F

        // If you're using `noIndex: true`, set `forceIgnoreNoIndex` to enable local index:
        // forceIgnoreNoIndex: true,
      }),
    ],
  ],

  plugins: [require.resolve('docusaurus-plugin-image-zoom')],

  /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
  themeConfig: {
    zoom: {
      selector: '.markdown :not(em) > img',
      background: {
        light: 'rgb(255, 255, 255)',
        dark: 'rgb(50, 50, 50)',
      },
      config: {
        margin: 24,
        scrollOffset: 0,
      },
    },
    docs: {
    sidebar: {
      hideable: true,
      autoCollapseCategories: true,
    },
  },
  navbar: {
    title: 'Documentação',
    items: [
      {
        type: 'docSidebar',
        sidebarId: 'tutorialSidebar',
        position: 'left',
        label: 'Ínicio',
      },
      {
        href: 'https://github.com/org-escritorio-adv/documentation',
        label: 'GitHub',
        position: 'right',
      },
    ],
  },
  footer: {
    links: [
      {
        title: 'Docs',
        items: [
          {
            label: 'Tutorial',
            to: '/docs/index',
          },
        ],
      },
      // {
      //   title: 'Community',
      //   items: [
      //     {
      //       label: 'Stack Overflow',
      //       href: 'https://stackoverflow.com/questions/tagged/docusaurus',
      //     },
      //     {
      //       label: 'Discord',
      //       href: 'https://discordapp.com/invite/docusaurus',
      //     },
      //     {
      //       label: 'X',
      //       href: 'https://x.com/docusaurus',
      //     },
      //   ],
      // },
      
    ],
    copyright: `Copyright © ${new Date().getFullYear()} Advocacia. Built with Docusaurus.`,
  },
  prism: {
       theme: prismThemes.github,
       darkTheme: prismThemes.dracula,
  },
  },
};

export default config;
