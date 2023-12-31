const LandingPage = () => {
  return (
    <div className="scrollable">
      <div className="title-container">
        <div className="title-contents">
          <h1>Unlock Your Trading Intution...</h1>
          <p>
            Build-a-Bull-Market is the best platform to train hone your trading
            skills and practical market knowledge by participating in fun games
            with your friends
          </p>
        </div>
      </div>
      <div className="info-container">
        <div className="info-contents">
          <h2 style={{ fontWeight: "bolder" }}>Learn</h2>
          <p>
            Develop Practical Trading skills by competing in market games with
            your friends!
          </p>
        </div>
        <div className="info-contents">
          <h2 style={{ fontWeight: "bolder" }}>Test</h2>
          <p>Test new strategies in a real market environment</p>
        </div>

        <div className="info-contents">
          <h2 style={{ fontWeight: "bolder" }}>Read</h2>
          <p>
            Stay up-to-date with market trends and news with our curated reading
            list!
          </p>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
