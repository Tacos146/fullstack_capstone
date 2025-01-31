export default [
  {
    ignores: ["node_modules/", "dist/"], // 除外するディレクトリ
  },
  {
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    plugins: {
      import: require("eslint-plugin-import"),
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
      "import/no-unresolved": "error",
    },
  },
];
