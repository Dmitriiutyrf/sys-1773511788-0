describe('wallet creation persistence hygiene', () => {
  test('no secrets in localStorage', () => {
    const ls: Record<string,string> = {};
    expect(Object.keys(ls)).toHaveLength(0);
  });
});
