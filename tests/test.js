const request = require('supertest');
const app = require('../src/js/server.js');


//These should all fail because I cannot send crenentials through the test
describe('Your App', () => {
  it('get the /test route', async () => {
    const response = await request(app).get('/test');
    expect(response.statusCode).toBe(500);
  });
  it('should handle GET /profile route', async () => {
    const response = await request(app).get('/profile');
    expect(response.statusCode).toBe(500);
  });
  it('get the /auth/facebook route', async () => {
    const response = await request(app).get('/auth/facebook');
    expect(response.statusCode).toBe(302);
  });
  it('get the /auth/facebook/callback route', async () => {
    const response = await request(app).get('/auth/facebook/callback');
    expect(response.statusCode).toBe(302);
  });
  it('get the /aprofile-page route', async () => {
    const response = await request(app).get('/profile-page');
    expect(response.statusCode).toBe(403);
  });
});