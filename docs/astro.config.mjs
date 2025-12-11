// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import starlightThemeRapide from 'starlight-theme-rapide';

// https://astro.build/config
export default defineConfig({
    site: 'https://totemlib.wavycat.me',
    integrations: [
        starlight({
            title: 'TotemLib',
            favicon: 'favicon.ico',
            locales: {
                root: {
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
                    label: 'Первые шаги',
                    translations: {
                        en: 'Start Here'
                    },
                    items: [
                        {
                            label: 'Введение',
                            translations: {
                                en: 'Getting Started',
                            },
                            slug: 'getting-started',
                        }
                    ]
                },
                {
                    label: 'Руководства',
                    translations: {
                        en: 'Guides',
                    },
                    items: [
                        {
                            label: 'Где получить скин?',
                            translations: {
                                en: 'How to Obtain a Skin?',
                            },
                            slug: 'guides/downloading-the-skin'
                        },
                        {
                            label: 'Как сгенерировать тотем?',
                            translations: {
                                en: 'How to Generate a Totem?',
                            },
                            slug: 'guides/generating-a-totem'
                        },
                        {
                            label: 'Как написать свой паттерн?',
                            translations: {
                                en: 'Writing Your Own Pattern',
                            },
                            slug: 'guides/writing-pattern'
                        },
                    ],
                },
                {
                    label: 'Концепты',
                    translations: {
                        en: 'Concepts',
                    },
                    items: [
                        {
                            label: 'Скин (Skin)',
                            translations: {
                                en: 'Skin',
                            },
                            slug: 'concepts/skin'
                        },
                        {
                            label: 'Паттерн (Pattern)',
                            translations: {
                                en: 'Pattern',
                            },
                            slug: 'concepts/pattern'
                        },
                        {
                            label: 'Билдер (Builder)',
                            translations: {
                                en: 'Builder',
                            },
                            slug: 'concepts/builder'
                        },
                        {
                            label: 'Тотем (Totem)',
                            translations: {
                                en: 'Totem',
                            },
                            slug: 'concepts/totem'
                        },
                    ]
                },
            ],
            plugins: [starlightThemeRapide(), starlightImageZoom()],
        }),
    ],
});
