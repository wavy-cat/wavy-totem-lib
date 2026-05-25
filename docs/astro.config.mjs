// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import starlightThemeRapide from 'starlight-theme-rapide';
import starlightPageActions from "starlight-page-actions";

// https://astro.build/config
export default defineConfig({
    site: 'https://totemlib.wavycat.me',
    integrations: [
        starlight({
            title: 'TotemLib',
            favicon: 'favicon.png',
            defaultLocale: 'en',
            locales: {
                en: {
                    label: 'English',
                    lang: 'en',
                },
                ru: {
                    label: 'Русский',
                    lang: 'ru',
                },
            },
            social: [
                { icon: 'github', label: 'GitHub', href: 'https://github.com/wavy-cat/wavy-totem-lib' },
                { icon: 'seti:python', label: 'PyPI', href: 'https://pypi.org/project/wavy-totem-lib' },
            ],
            editLink: {
                baseUrl: 'https://github.com/wavy-cat/wavy-totem-lib/edit/main/docs/',
            },
            sidebar: [
                {
                    label: 'Start Here',
                    translations: {
                        ru: 'Первые шаги'
                    },
                    items: [
                        {
                            label: 'Getting Started',
                            translations: {
                                ru: 'Введение',
                            },
                            slug: 'getting-started',
                        }
                    ]
                },
                {
                    label: 'Guides',
                    translations: {
                        ru: 'Руководства',
                    },
                    items: [
                        {
                            label: 'How to get a skin?',
                            translations: {
                                ru: 'Где получить скин?',
                            },
                            slug: 'guides/downloading-the-skin'
                        },
                        {
                            label: 'How to generate a totem?',
                            translations: {
                                ru: 'Как сгенерировать тотем?',
                            },
                            slug: 'guides/generating-a-totem'
                        },
                        {
                            label: 'Writing your own pattern',
                            translations: {
                                ru: 'Написание своего паттерна',
                            },
                            slug: 'guides/writing-pattern'
                        },
                    ],
                },
                {
                    label: 'Concepts',
                    translations: {
                        ru: 'Концепты',
                    },
                    items: [
                        {
                            label: 'Skin',
                            translations: {
                                ru: 'Скин (Skin)',
                            },
                            slug: 'concepts/skin'
                        },
                        {
                            label: 'Pattern',
                            translations: {
                                ru: 'Паттерн (Pattern)',
                            },
                            slug: 'concepts/pattern'
                        },
                        {
                            label: 'Builder',
                            translations: {
                                ru: 'Билдер (Builder)',
                            },
                            slug: 'concepts/builder'
                        },
                        {
                            label: 'Totem',
                            translations: {
                                ru: 'Тотем (Totem)',
                            },
                            slug: 'concepts/totem'
                        },
                    ]
                },
            ],
            plugins: [
                starlightThemeRapide(),
                starlightImageZoom(),
                starlightPageActions({
                    baseUrl: "https://totemlib.wavycat.me",
                    share: true,
                    actions: {
                        perplexity: true
                    }
                })
            ],
        }),
    ],
    prefetch: false,
});
