import streamlit.components.v1 as components


def render_network_background() -> None:
    components.html(
        """
        <script>
          (function() {
            const existing = window.parent.document.getElementById('bg-network-canvas');
            if (existing) return;

            const canvas = window.parent.document.createElement('canvas');
            canvas.id = 'bg-network-canvas';
            canvas.style.position = 'fixed';
            canvas.style.inset = '0';
            canvas.style.width = '100vw';
            canvas.style.height = '100vh';
            canvas.style.zIndex = '0';
            canvas.style.pointerEvents = 'none';
            window.parent.document.body.appendChild(canvas);

            const ctx = canvas.getContext('2d');
            const dpr = window.devicePixelRatio || 1;

            const resize = () => {
              canvas.width = window.innerWidth * dpr;
              canvas.height = window.innerHeight * dpr;
              ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            };
            resize();
            window.parent.addEventListener('resize', resize);

            const nodes = [];
            const nodeCount = 45;
            const maxDist = 140;

            for (let i = 0; i < nodeCount; i++) {
              nodes.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                vx: (Math.random() - 0.5) * 0.25,
                vy: (Math.random() - 0.5) * 0.25,
              });
            }

            function step() {
              ctx.clearRect(0, 0, canvas.width, canvas.height);

              for (const n of nodes) {
                n.x += n.vx;
                n.y += n.vy;
                if (n.x < 0 || n.x > window.innerWidth) n.vx *= -1;
                if (n.y < 0 || n.y > window.innerHeight) n.vy *= -1;
              }

              for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                  const a = nodes[i];
                  const b = nodes[j];
                  const dx = a.x - b.x;
                  const dy = a.y - b.y;
                  const dist = Math.sqrt(dx * dx + dy * dy);
                  if (dist < maxDist) {
                    const alpha = 0.18 * (1 - dist / maxDist);
                    ctx.strokeStyle = `rgba(74, 163, 223, ${alpha})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(a.x, a.y);
                    ctx.lineTo(b.x, b.y);
                    ctx.stroke();
                  }
                }
              }

              for (const n of nodes) {
                ctx.fillStyle = 'rgba(74, 163, 223, 0.35)';
                ctx.beginPath();
                ctx.arc(n.x, n.y, 2.3, 0, Math.PI * 2);
                ctx.fill();
              }

              window.parent.requestAnimationFrame(step);
            }

            step();
          })();
        </script>
        """,
        height=0,
    )
