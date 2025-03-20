import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  let res = http.post('http://localhost:5000/wave', JSON.stringify({ name: 'Test User' }), {
    headers: { 'Content-Type': 'application/json' },
  });
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}