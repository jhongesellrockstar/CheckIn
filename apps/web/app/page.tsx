import { greet } from '@checkin/shared';

export default function Page() {
  return (
    <main>
      <h1>{greet('CheckIn')}</h1>
      <p>API URL: {process.env.NEXT_PUBLIC_API_URL}</p>
    </main>
  );
}
