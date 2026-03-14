export type DataSignature = { coseSign1: Uint8Array; };
export async function signData(input: Uint8Array): Promise<DataSignature> {
  return { coseSign1: input };
}
export async function verifySignature(sig: DataSignature): Promise<boolean> {
  return !!sig && !!sig.coseSign1 && sig.coseSign1.length > 0;
}
