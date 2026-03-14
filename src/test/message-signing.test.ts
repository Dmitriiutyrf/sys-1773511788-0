import { signData, verifySignature } from '../lib/cardano/messageSigning';
test('CIP-8 sign/verify pass', async () => {
  const payload = new Uint8Array([1,2,3]);
  const sig = await signData(payload);
  expect(await verifySignature(sig)).toBe(true);
});
